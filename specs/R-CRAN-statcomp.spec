%global packname  statcomp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Complexity and Information Measures for Time SeriesAnalysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7.0
Requires:         R-core >= 2.7.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-Matrix 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-zoo 
Requires:         R-Matrix 
Requires:         R-graphics 

%description
An implementation of local and global statistical complexity measures (aka
Information Theory Quantifiers, ITQ) for time series analysis based on
ordinal statistics (Bandt and Pompe (2002)
<DOI:10.1103/PhysRevLett.88.174102>). Several distance measures that
operate on ordinal pattern distributions, auxiliary functions for ordinal
pattern analysis, and generating functions for stochastic and
deterministic-chaotic processes for ITQ testing are provided.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
