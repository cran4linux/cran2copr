%global packname  processcheckR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Rule-Based Conformance Checking of Business Process Event Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-bupaR 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-edeaR 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-bupaR 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-edeaR 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-glue 

%description
Check compliance of event-data from (business) processes with respect to
specified rules. Rules supported are of three types: frequency (activities
that should (not) happen x number of times), order (succession between
activities) and exclusiveness (and and exclusive choice between
activities).

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
