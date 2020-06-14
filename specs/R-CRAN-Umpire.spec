%global packname  Umpire
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          2%{?dist}
Summary:          Simulating Realistic Gene Expression and Clinical Data

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mc2d 
BuildRequires:    R-CRAN-BimodalIndex 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-mc2d 
Requires:         R-CRAN-BimodalIndex 

%description
The Ultimate Microrray Prediction, Reality and Inference Engine (UMPIRE)
is a package to facilitate the simulation of realistic microarray data
sets with links to associated outcomes. See Zhang and Coombes (2012)
<doi:10.1186/1471-2105-13-S13-S1>. Version 2.0 adds the ability to
simulate realistic mixed-typed clinical data.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
