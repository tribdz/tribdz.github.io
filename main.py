import json
from pathlib import Path

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput


class QuanLyThuChiApp(App):

    def build(self):

        # Android-writable location for mobile_data.json
        self.data_file = Path(self.user_data_dir) / "mobile_data.json"

        self.expenses = [
            {"name": "Điện"},
            {"name": "Nước"},
            {"name": "Đóng học cho Bình"},
            {"name": "Đóng học cho Bống"},
            {"name": "Ăn"},
            {"name": "Tiêu vặt"},
            {"name": "Quan hệ"},
            {"name": "Xăng xe"},
            {"name": "Điện thoại"},
        ]

        self.incomes = [
            {"name": "Lương của mẹ"},
            {"name": "Lương của bố"},
            {"name": "Thu nhập khác"},
        ]

        # ==================== MAIN LAYOUT ====================

        root = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(10)
        )

        title = Label(
            text="Quản lý thu chi",
            font_size=dp(28),
            size_hint_y=None,
            height=dp(50)
        )

        root.add_widget(title)

        # ==================== MONTH / YEAR ====================

        date_layout = BoxLayout(
            spacing=dp(10),
            size_hint_y=None,
            height=dp(50)
        )

        self.month = Spinner(
            text="Tháng 1",
            values=[f"Tháng {i}" for i in range(1, 13)]
        )

        self.year = Spinner(
            text="Năm 2026",
            values=[f"Năm {i}" for i in range(2020, 2036)]
        )

        date_layout.add_widget(self.month)
        date_layout.add_widget(self.year)

        root.add_widget(date_layout)

        self.month.bind(text=self.load_data)
        self.year.bind(text=self.load_data)

        # ==================== SCROLL ====================

        scroll = ScrollView()

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(15),
            padding=dp(5),
            size_hint_y=None
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        scroll.add_widget(content)
        root.add_widget(scroll)

        # ==================== THU ====================

        self.thu_box = self.create_section(
            "THU",
            self.incomes,
            "Thêm thu nhập"
        )

        content.add_widget(self.thu_box)

        # ==================== CHI ====================

        self.chi_box = self.create_section(
            "CHI",
            self.expenses,
            "Thêm chi tiêu"
        )

        content.add_widget(self.chi_box)

        # ==================== TOTALS ====================

        self.previous_balance_label = Label(
            text="Số dư tháng trước: 0 VND",
            size_hint_y=None,
            height=dp(40)
        )

        self.total_money_label = Label(
            text="Tiền còn lại: 0 VND",
            font_size=dp(20),
            size_hint_y=None,
            height=dp(45)
        )

        content.add_widget(self.previous_balance_label)
        content.add_widget(self.total_money_label)

        # ==================== SAVE ====================

        save_button = Button(
            text="Lưu thay đổi",
            size_hint_y=None,
            height=dp(50)
        )

        save_button.bind(
            on_press=self.save_changes
        )

        content.add_widget(save_button)

        self.load_data()

        return root

    # ==================== SECTION ====================

    def create_section(self, title, items, add_text):

        box = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
            size_hint_y=None
        )

        box.bind(
            minimum_height=box.setter("height")
        )

        box.add_widget(
            Label(
                text=title,
                font_size=dp(22),
                size_hint_y=None,
                height=dp(40)
            )
        )

        rows = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
            size_hint_y=None
        )

        rows.bind(
            minimum_height=rows.setter("height")
        )

        box.add_widget(rows)

        box.rows = rows

        for item in items:
            self.create_row(item, rows)

        button = Button(
            text=add_text,
            size_hint_y=None,
            height=dp(48)
        )

        if items is self.incomes:
            button.bind(on_press=self.add_income)
        else:
            button.bind(on_press=self.add_expense)

        box.add_widget(button)

        total_label = Label(
            text="Tổng: 0 VND",
            size_hint_y=None,
            height=dp(40)
        )

        box.add_widget(total_label)

        if items is self.incomes:
            self.total_income_label = total_label
        else:
            self.total_pay_label = total_label

        return box

    # ==================== CREATE ROW ====================

    def create_row(self, item, parent):

        row = BoxLayout(
            orientation="horizontal",
            spacing=dp(8),
            size_hint_y=None,
            height=dp(45)
        )

        name_input = TextInput(
            text=item["name"],
            multiline=False
        )

        amount_input = TextInput(
            text="0",
            multiline=False,
            input_filter="int"
        )

        row.add_widget(name_input)
        row.add_widget(amount_input)

        parent.add_widget(row)

        item["name_input"] = name_input
        item["input"] = amount_input

    # ==================== ADD ROW ====================

    def add_item(self, items, rows, default_name):

        item = {"name": default_name}

        items.append(item)

        self.create_row(item, rows)

    def add_income(self, instance):

        self.add_item(
            self.incomes,
            self.thu_box.rows,
            "Thu nhập mới"
        )

    def add_expense(self, instance):

        self.add_item(
            self.expenses,
            self.chi_box.rows,
            "Chi tiêu mới"
        )

    # ==================== DATA ====================

    def read_data(self):

        try:
            with open(
                self.data_file,
                "r",
                encoding="utf-8"
            ) as file:
                return json.load(file)

        except FileNotFoundError:
            return {}

    def get_value(self, input_box):

        try:
            return int(input_box.text or 0)

        except ValueError:
            return 0

    # ==================== PREVIOUS MONTH ====================

    def get_previous_key(self):

        selected_month = (
            self.month.values.index(self.month.text) + 1
        )

        selected_year = int(
            self.year.text.replace("Năm ", "")
        )

        if selected_month == 1:
            previous_month = 12
            previous_year = selected_year - 1

        else:
            previous_month = selected_month - 1
            previous_year = selected_year

        return f"Năm {previous_year}-Tháng {previous_month}"

    # ==================== TOTALS ====================

    def update_totals(self):

        total_pay = sum(
            self.get_value(item["input"])
            for item in self.expenses
        )

        total_income = sum(
            self.get_value(item["input"])
            for item in self.incomes
        )

        data = self.read_data()

        previous_data = data.get(
            self.get_previous_key()
        )

        previous_balance = (
            previous_data.get("balance", 0)
            if previous_data
            else 0
        )

        total_money = (
            previous_balance
            + total_income
            - total_pay
        )

        self.total_pay_label.text = (
            f"Tổng chi: {total_pay:,} VND"
        )

        self.total_income_label.text = (
            f"Tổng thu: {total_income:,} VND"
        )

        self.previous_balance_label.text = (
            f"Số dư tháng trước: "
            f"{previous_balance:,} VND"
        )

        self.total_money_label.text = (
            f"Tiền còn lại: {total_money:,} VND"
        )

    # ==================== SAVE ====================

    def save_changes(self, instance=None):

        data = self.read_data()

        key = f"{self.year.text}-{self.month.text}"

        total_pay = sum(
            self.get_value(item["input"])
            for item in self.expenses
        )

        total_income = sum(
            self.get_value(item["input"])
            for item in self.incomes
        )

        previous_data = data.get(
            self.get_previous_key()
        )

        previous_balance = (
            previous_data.get("balance", 0)
            if previous_data
            else 0
        )

        total_money = (
            previous_balance
            + total_income
            - total_pay
        )

        # Global names

        data["expense_names"] = [
            item["name_input"].text
            for item in self.expenses
        ]

        data["income_names"] = [
            item["name_input"].text
            for item in self.incomes
        ]

        # Current month

        data[key] = {
            "incomes": [
                {
                    "value": self.get_value(
                        item["input"]
                    )
                }
                for item in self.incomes
            ],

            "expenses": [
                {
                    "value": self.get_value(
                        item["input"]
                    )
                }
                for item in self.expenses
            ],

            "balance": total_money
        }

        with open(
            self.data_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

        self.update_totals()

    # ==================== LOAD ====================

    def load_data(self, *args):

        data = self.read_data()

        saved_expense_names = data.get(
            "expense_names",
            []
        )

        saved_income_names = data.get(
            "income_names",
            []
        )

        # Add missing rows

        while len(self.expenses) < len(
            saved_expense_names
        ):
            self.add_expense(None)

        while len(self.incomes) < len(
            saved_income_names
        ):
            self.add_income(None)

        # Load global names

        for item, name in zip(
            self.expenses,
            saved_expense_names
        ):
            item["name_input"].text = name

        for item, name in zip(
            self.incomes,
            saved_income_names
        ):
            item["name_input"].text = name

        # Current month

        key = f"{self.year.text}-{self.month.text}"

        saved_data = data.get(key)

        if saved_data is None:

            for item in self.incomes:
                item["input"].text = "0"

            for item in self.expenses:
                item["input"].text = "0"

        else:

            saved_incomes = saved_data.get(
                "incomes",
                []
            )

            saved_expenses = saved_data.get(
                "expenses",
                []
            )

            # Make sure enough rows exist

            while len(self.incomes) < len(
                saved_incomes
            ):
                self.add_income(None)

            while len(self.expenses) < len(
                saved_expenses
            ):
                self.add_expense(None)

            # Load values

            for item, saved in zip(
                self.incomes,
                saved_incomes
            ):
                item["input"].text = str(
                    saved.get("value", 0)
                )

            for item, saved in zip(
                self.expenses,
                saved_expenses
            ):
                item["input"].text = str(
                    saved.get("value", 0)
                )

        self.update_totals()


if __name__ == "__main__":
    QuanLyThuChiApp().run()
