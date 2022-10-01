%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  depigner
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Utility Package to Help you Deal with "Pignas"

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-rms >= 5.1.2
BuildRequires:    R-CRAN-Hmisc >= 4.2.0
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-telegram.bot >= 2.3.0
BuildRequires:    R-CRAN-usethis >= 1.5.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-progress >= 1.2.0
BuildRequires:    R-CRAN-tidyr >= 0.8.1
BuildRequires:    R-CRAN-dplyr >= 0.7.7
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-rlang >= 0.2.2
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-rms >= 5.1.2
Requires:         R-CRAN-Hmisc >= 4.2.0
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-telegram.bot >= 2.3.0
Requires:         R-CRAN-usethis >= 1.5.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-progress >= 1.2.0
Requires:         R-CRAN-tidyr >= 0.8.1
Requires:         R-CRAN-dplyr >= 0.7.7
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-rlang >= 0.2.2
Requires:         R-CRAN-desc 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rprojroot 
Requires:         R-stats 
Requires:         R-utils 

%description
Pigna [_pìn'n'a_] is the Italian word for pine cone.  In jargon, it is
used to identify a task which is boring, banal, annoying, painful,
frustrating and maybe even with a not so beautiful or rewarding result,
just like the obstinate act of trying to challenge yourself in extracting
pine nuts from a pine cone, provided that, in the end, you will find at
least one inside it. Here you can find a backpack of functions to be used
to solve small everyday problems of coding or analyzing (clinical) data,
which would be normally solved using quick-and-dirty patches. You will be
able to convert 'Hmisc' and 'rms' summary()es into data.frames ready to be
rendered by 'pander' and 'knitr'. You can access easy-to-use wrappers to
activate essential but useful progress bars (from 'progress') into your
loops or functionals. Easy setup and control Telegram's bots (from
'telegram.bot') to send messages or to divert error messages to a
Telegram's chat. You also have some utilities helping you in the
development of packages, like the activation of the same user interface of
'usethis' into your package, or call polite functions to ask a user to
install other packages. Finally, you find a set of thematic sets of
packages you may use to set up new environments quickly, installing them
in a single call.

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
