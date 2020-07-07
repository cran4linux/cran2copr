%global packname  ptw
%global packver   1.9-15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.15
Release:          3%{?dist}
Summary:          Parametric Time Warping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-nloptr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Parametric Time Warping aligns patterns, i.e. it aims to put corresponding
features at the same locations. The algorithm searches for an optimal
polynomial describing the warping. It is possible to align one sample to a
reference, several samples to the same reference, or several samples to
several references. One can choose between calculating individual
warpings, or one global warping for a set of samples and one reference.
Two optimization criteria are implemented: RMS (Root Mean Square error)
and WCC (Weighted Cross Correlation). Both warping of peak profiles and of
peak lists are supported. A vignette for the latter is contained in the
inst/doc directory of the source package - the vignette source can be
found on the package github site.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
