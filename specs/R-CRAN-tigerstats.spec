%global __brp_check_rpaths %{nil}
%global packname  tigerstats
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          2%{?dist}%{?buildtag}
Summary:          R Functions for Elementary Statistics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-abd 
BuildRequires:    R-CRAN-mosaic 
BuildRequires:    R-CRAN-mosaicData 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-manipulate 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-abd 
Requires:         R-CRAN-mosaic 
Requires:         R-CRAN-mosaicData 
Requires:         R-CRAN-ggplot2 
Requires:         R-lattice 
Requires:         R-CRAN-manipulate 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-rlang 

%description
A collection of data sets and functions that are useful in the teaching of
statistics at an elementary level to students who may have little or no
previous experience with the command line.  The functions for elementary
inferential procedures follow a uniform interface for user input.  Some of
the functions are instructional applets that can only be run on the R
Studio integrated development environment with package 'manipulate'
installed.  Other instructional applets are Shiny apps that may be run
locally. In teaching the package is used alongside of package 'mosaic',
'mosaicData' and 'abd', which are therefore listed as dependencies.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/CentralLimit
%doc %{rlibdir}/%{packname}/CIMean
%doc %{rlibdir}/%{packname}/CoinFlip
%doc %{rlibdir}/%{packname}/FindRegLine
%doc %{rlibdir}/%{packname}/RandomExpBinom
%doc %{rlibdir}/%{packname}/SamplingMethods
%doc %{rlibdir}/%{packname}/ShallowReg
%doc %{rlibdir}/%{packname}/SlowGoodness
%doc %{rlibdir}/%{packname}/Type12Errors
%{rlibdir}/%{packname}/INDEX
