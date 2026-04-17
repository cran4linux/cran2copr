%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rquiz
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Quizzes as HTML Widgets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.7.0
BuildRequires:    R-CRAN-htmlwidgets >= 1.5.0
Requires:         R-CRAN-jsonlite >= 1.7.0
Requires:         R-CRAN-htmlwidgets >= 1.5.0

%description
Creates interactive JavaScript-based quizzes as 'HTML' widgets. Offers
three quiz types: a single question with instant feedback
(singleQuestion()), a multi-question quiz with navigation, timer, and
results (multiQuestions()), and fill-in-the-blank cloze exercises
(fillBlanks()). All quizzes auto-detect single-choice and multiple-choice
modes from the input data, support customizable styling, keyboard
navigation, and multilingual UI (English, German, French, Spanish).
Designed for use in 'R Markdown', 'Quarto', and 'Shiny' applications. The
singleQuestion() quiz design was inspired by Ozzie Kirkby
<https://codepen.io/ozzie/pen/pvrVLm>. The multiQuestions() quiz design
was inspired by Abhilash Narayan
<https://codepen.io/abhilashn/pen/BRepQz>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
