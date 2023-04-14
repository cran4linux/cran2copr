%global __brp_check_rpaths %{nil}
%global packname  DIFlasso
%global packver   1.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          A Penalty Approach to Differential Item Functioning in RaschModels

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-grplasso 
BuildRequires:    R-CRAN-penalized 
BuildRequires:    R-CRAN-miscTools 
Requires:         R-CRAN-grplasso 
Requires:         R-CRAN-penalized 
Requires:         R-CRAN-miscTools 

%description
Performs DIFlasso as proposed by Tutz and Schauberger (2015)
<doi:10.1007/s11336-013-9377-6>, a method to detect DIF (Differential Item
Functioning) in Rasch Models. It can handle settings with many variables
and also metric variables.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
