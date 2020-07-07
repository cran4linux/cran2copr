%global packname  RcmdrPlugin.depthTools
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}
Summary:          R commander Depth Tools Plug-In

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 1.4.0
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-depthTools 
Requires:         R-CRAN-Rcmdr >= 1.4.0
Requires:         R-tcltk 
Requires:         R-CRAN-depthTools 

%description
This package provides an Rcmdr plug-in based on the depthTools package,
which implements different robust statistical tools for the description
and analysis of gene expression data based on the Modified Band Depth,
namely, the scale curves for visualizing the dispersion of one or various
groups of samples (e.g. types of tumors), a rank test to decide whether
two groups of samples come from a single distribution and two methods of
supervised classification techniques, the DS and TAD methods.

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
%doc %{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/INDEX
