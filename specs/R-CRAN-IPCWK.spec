%global packname  IPCWK
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Kendall's Tau Partial Corr. for Survival Trait and Biomarkers

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.3
Requires:         R-core >= 3.4.3
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-survival 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-MASS 
Requires:         R-survival 
Requires:         R-stats 
Requires:         R-utils 

%description
We propose the inverse probability-of-censoring weighted (IPCW) Kendall's
tau to measure the association of the survival trait with biomarkers and
Kendall's partial correlation to reflect the relationship of the survival
trait with interaction variable conditional on main effects, as described
in Wang and Chen (2020) <doi:10.1093/bioinformatics/btaa017>.

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
%{rlibdir}/%{packname}/INDEX
