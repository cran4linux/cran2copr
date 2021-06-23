%global __brp_check_rpaths %{nil}
%global packname  CPP
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Composition of Probabilistic Preferences (CPP)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.0
Requires:         R-core >= 2.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ineq 
BuildRequires:    R-CRAN-kappalab 
BuildRequires:    R-CRAN-mc2d 
Requires:         R-CRAN-ineq 
Requires:         R-CRAN-kappalab 
Requires:         R-CRAN-mc2d 

%description
CPP is a multiple criteria decision method to evaluate alternatives on
complex decision making problems, by a probabilistic approach. The CPP was
created and expanded by Sant'Anna, Annibal P. (2015)
<doi:10.1007/978-3-319-11277-0>.

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
%{rlibdir}/%{packname}/INDEX
