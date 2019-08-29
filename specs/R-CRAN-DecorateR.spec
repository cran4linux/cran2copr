%global packname  DecorateR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Fit and Deploy DECORATE Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RWeka 
BuildRequires:    R-CRAN-RWekajars 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-stats 
Requires:         R-CRAN-RWeka 
Requires:         R-CRAN-RWekajars 
Requires:         R-CRAN-rJava 
Requires:         R-stats 

%description
DECORATE (Diverse Ensemble Creation by Oppositional Relabeling of
Artificial Training Examples) builds an ensemble of J48 trees by
recursively adding artificial samples of the training data ("Melville, P.,
& Mooney, R. J. (2005). Creating diversity in ensembles using artificial
data. Information Fusion, 6(1), 99-111.
<doi:10.1016/j.inffus.2004.04.001>").

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
