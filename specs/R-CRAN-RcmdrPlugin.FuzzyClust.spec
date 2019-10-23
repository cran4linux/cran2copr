%global packname  RcmdrPlugin.FuzzyClust
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          R Commander Plug-in for Fuzzy Clustering Methods (Fuzzy C-Meansand Gustafson Kessel)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-parallel 
Requires:         R-CRAN-Rcmdr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-tkrplot 
Requires:         R-CRAN-iterators 
Requires:         R-parallel 

%description
The R Commander Plug-in for Fuzzy Clustering Methods. This Plug- in
provide Graphical User Interface of 2 methods of Fuzzy Clustering (Fuzzy
C- Means /FCM and Gustafson Kessel-Babuska). For validation of clustering,
this plug- in use Xie Beni Index, MPC index, and CE index. For statistical
test (test of significant differences of grouping/clustering), this
plug-in use MANOVA analysis with Pillai trace statistics. For stabilize
the result, this package provide soft voting cluster ensemble function.
Visualization of result are provided via plugin that must be load in Rcmdr
file.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/Report.Rmd
%{rlibdir}/%{packname}/INDEX
