%global packname  sharx
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          3%{?dist}%{?buildtag}
Summary:          Models and Data Sets for the Study of Species-Area Relationships

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-dcmle 
BuildRequires:    R-CRAN-dclone 
Requires:         R-methods 
Requires:         R-stats4 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-dcmle 
Requires:         R-CRAN-dclone 

%description
Hierarchical models for the analysis of species-area relationships (SARs)
by combining several data sets and covariates; with a global data set
combining individual SAR studies; as described in Solymos and Lele (2012,
Global Ecology and Biogeography 21, 109-120).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/sardata.bib
%{rlibdir}/%{packname}/sardata.txt
%{rlibdir}/%{packname}/INDEX
