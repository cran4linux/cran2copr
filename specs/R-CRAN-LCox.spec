%global packname  LCox
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          A Tool for Selecting Genes Related to Survival Outcomes usingLongitudinal Gene Expression Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-survival >= 2.41.3
BuildRequires:    R-CRAN-fdapace >= 0.3.0
Requires:         R-survival >= 2.41.3
Requires:         R-CRAN-fdapace >= 0.3.0

%description
Longitudinal genomics data and survival outcome are common in biomedical
studies. It is of great interest to select genes related to the survival
outcome. LCox is a computationally efficient tool for selecting genes
related to the survival outcome using the longitudinal genomics data. LCox
is powerful to detect different forms of dependence between the
longitudinal biomarkers and the survival outcome.

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
