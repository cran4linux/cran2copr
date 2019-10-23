%global packname  ruv
%global packver   0.9.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7.1
Release:          1%{?dist}
Summary:          Detect and Remove Unwanted Variation using Negative Controls

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gridExtra 

%description
Implements the 'RUV' (Remove Unwanted Variation) algorithms.  These
algorithms attempt to adjust for systematic errors of unknown origin in
high-dimensional data.  The algorithms were originally developed for use
with genomic data, especially microarray data, but may be useful with
other types of high-dimensional data as well.  These algorithms were
proposed in Gagnon-Bartsch and Speed (2012) <doi:10.1093/nar/gkz433>,
Gagnon-Bartsch, Jacob and Speed (2013), and Molania, et. al. (2019)
<doi:10.1093/nar/gkz433>.  The algorithms require the user to specify a
set of negative control variables, as described in the references.  The
algorithms included in this package are 'RUV-2', 'RUV-4', 'RUV-inv',
'RUV-rinv', 'RUV-I', and RUV-III', along with various supporting
algorithms.

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
%{rlibdir}/%{packname}/libs
