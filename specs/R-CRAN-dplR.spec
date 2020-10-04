%global packname  dplR
%global packver   1.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.1
Release:          3%{?dist}%{?buildtag}
Summary:          Dendrochronology Program Library in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.2
Requires:         R-core >= 2.15.2
BuildRequires:    R-CRAN-XML >= 2.1.0
BuildRequires:    R-CRAN-plyr >= 1.8
BuildRequires:    R-CRAN-R.utils >= 1.32.1
BuildRequires:    R-Matrix >= 1.0.3
BuildRequires:    R-CRAN-matrixStats >= 0.50.2
BuildRequires:    R-CRAN-stringr >= 0.4
BuildRequires:    R-CRAN-digest >= 0.2.3
BuildRequires:    R-CRAN-stringi >= 0.2.3
BuildRequires:    R-lattice >= 0.13.6
BuildRequires:    R-CRAN-png >= 0.1.2
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-signal 
Requires:         R-CRAN-XML >= 2.1.0
Requires:         R-CRAN-plyr >= 1.8
Requires:         R-CRAN-R.utils >= 1.32.1
Requires:         R-Matrix >= 1.0.3
Requires:         R-CRAN-matrixStats >= 0.50.2
Requires:         R-CRAN-stringr >= 0.4
Requires:         R-CRAN-digest >= 0.2.3
Requires:         R-CRAN-stringi >= 0.2.3
Requires:         R-lattice >= 0.13.6
Requires:         R-CRAN-png >= 0.1.2
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-signal 

%description
Perform tree-ring analyses such as detrending, chronology building, and
cross dating.  Read and write standard file formats used in
dendrochronology.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
