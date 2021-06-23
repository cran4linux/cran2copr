%global __brp_check_rpaths %{nil}
%global packname  ABPS
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}%{?buildtag}
Summary:          The Abnormal Blood Profile Score to Detect Blood Doping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-kernlab 
Requires:         R-CRAN-kernlab 

%description
An implementation of the Abnormal Blood Profile Score (ABPS, part of the
Athlete Biological Passport program of the World Anti-Doping Agency),
which combines several blood parameters into a single score in order to
detect blood doping (Sottas et al. (2006) <doi:10.2202/1557-4679.1011>).
The package also contains functions to calculate other scores used in
anti-doping programs, such as the OFF-score (Gore et al. (2003)
<http://www.haematologica.org/content/88/3/333>), as well as example data.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
