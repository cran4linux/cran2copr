%global packname  manymodelr
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          Build and Tune Several Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0.81
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-e1071 >= 1.7.0.1
BuildRequires:    R-CRAN-lme4 >= 1.1.23
BuildRequires:    R-CRAN-dplyr >= 0.8.9
BuildRequires:    R-CRAN-Metrics >= 0.1.4
Requires:         R-CRAN-caret >= 6.0.81
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-e1071 >= 1.7.0.1
Requires:         R-CRAN-lme4 >= 1.1.23
Requires:         R-CRAN-dplyr >= 0.8.9
Requires:         R-CRAN-Metrics >= 0.1.4

%description
Frequently one needs a convenient way to build and tune several models in
one go.The goal is to provide a number of machine learning convenience
functions. It provides the ability to build, tune and obtain predictions
of several models in one function. The models are built using 'caret'
functions with easier to read syntax. Kuhn(2014) <arXiv:1405.6974>.

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
