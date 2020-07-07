%global packname  vegan3d
%global packver   1.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}
Summary:          Static and Dynamic 3D Plots for the 'vegan' Package

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan >= 2.3.0
BuildRequires:    R-CRAN-scatterplot3d >= 0.3.40
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-vegan >= 2.3.0
Requires:         R-CRAN-scatterplot3d >= 0.3.40
Requires:         R-cluster 
Requires:         R-CRAN-rgl 

%description
Static and dynamic 3D plots to be used with ordination results and in
diversity analysis, especially with the vegan package.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/README.md
%{rlibdir}/%{packname}/INDEX
