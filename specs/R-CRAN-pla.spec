%global packname  pla
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Parallel Line Assays

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Parallel Line Assays: Completely randomized design, Randomized Block
design, and Latin squares design. Balanced data are fitted as described in
the Ph.Eur. In the presence of missing values complete data analysis can
be performed (with computation of Fieller's confidence intervals for the
estimated potency), or imputation of values can be applied. The package
contains a script such that a pdf-document with a report of an analysis of
an assay can be produced from an input file with data of the assay. Here
no knowledge of R is needed by the user.

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
%doc %{rlibdir}/%{packname}/R.xtables
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/vignettes
%{rlibdir}/%{packname}/INDEX
