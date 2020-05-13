%global packname  scales
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Scale Functions for Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-farver >= 2.0.3
BuildRequires:    R-CRAN-munsell >= 0.5
BuildRequires:    R-CRAN-labeling 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-farver >= 2.0.3
Requires:         R-CRAN-munsell >= 0.5
Requires:         R-CRAN-labeling 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-viridisLite 

%description
Graphical scales map data to aesthetics, and provide methods for
automatically determining breaks and labels for axes and legends.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
