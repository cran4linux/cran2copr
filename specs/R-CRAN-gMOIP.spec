%global packname  gMOIP
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}
Summary:          '2D and 3D plots of linear mathematical programming models'

License:          GPL (>= 3.3.2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rgl 
Requires:         R-MASS 
Requires:         R-CRAN-plyr 

%description
Make 2D and 3D plots of the polytope of a LP, ILP or MILP problem,
including integer points and iso profit curve. Can also make a plot of the
bi-objective criterion space.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
