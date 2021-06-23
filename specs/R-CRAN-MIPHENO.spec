%global __brp_check_rpaths %{nil}
%global packname  MIPHENO
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Mutant Identification through Probabilistic High throughputEnabled NOrmalization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.1
Requires:         R-core >= 2.12.1
BuildArch:        noarch
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-gdata 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-gdata 

%description
This package contains functions to carry out processing of high throughput
data analysis and detection of putative hits/mutants.  Contents include a
function for post-hoc quality control for removal of outlier sample sets,
a median-based normalization method for use in datasets where there are no
explicit controls and where most of the responses are of the wildtype/no
response class (see accompanying paper).  The package also includes a way
to prioritize individuals of interest using am empirical cumulative
distribution function. Methods for generating synthetic data as well as
data from the Chloroplast 2010 project are included.

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
