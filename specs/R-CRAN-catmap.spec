%global packname  catmap
%global packver   1.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.4
Release:          3%{?dist}%{?buildtag}
Summary:          Case-Control and TDT Meta-Analysis Package

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-forestplot 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-metafor 
Requires:         R-stats 
Requires:         R-CRAN-forestplot 
Requires:         R-grid 
Requires:         R-CRAN-metafor 

%description
Although many software tools can perform meta-analyses on genetic
case-control data, none of these apply to combined case-control and
family-based (TDT) studies. This package conducts fixed-effects (with
inverse variance weighting) and random-effects [DerSimonian and Laird
(1986) <DOI:10.1016/0197-2456(86)90046-2>] meta-analyses on combined
genetic data. Specifically, this package implements a fixed-effects model
[Kazeem and Farrall (2005) <DOI:10.1046/j.1529-8817.2005.00156.x>] and a
random-effects model [Nicodemus (2008) <DOI:10.1186/1471-2105-9-130>] for
combined studies.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
