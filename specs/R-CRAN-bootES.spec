%global __brp_check_rpaths %{nil}
%global packname  bootES
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Bootstrap Effect Sizes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.1
Requires:         R-core >= 2.10.1
BuildArch:        noarch
BuildRequires:    R-boot 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-boot 
Requires:         R-stats 
Requires:         R-graphics 

%description
Calculate robust measures of effect sizes using the bootstrap.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/commands.txt
%doc %{rlibdir}/%{packname}/example.csv
%doc %{rlibdir}/%{packname}/monte_carlo.R
%doc %{rlibdir}/%{packname}/robust_d_test.csv
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
