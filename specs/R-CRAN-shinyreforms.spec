%global __brp_check_rpaths %{nil}
%global packname  shinyreforms
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Add Forms to your 'Shiny' App

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.0.0
BuildRequires:    R-CRAN-htmltools >= 0.2.6
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-shiny >= 1.0.0
Requires:         R-CRAN-htmltools >= 0.2.6
Requires:         R-CRAN-R6 

%description
Allows to create modular, reusable 'HTML' forms which can be embedded in
your 'shiny' app with minimal effort. Features include conditional code
execution on form submission, automatic input validation and input
tooltips.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
