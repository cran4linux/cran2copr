%global packname  forestRK
%global packver   0.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}
Summary:          Implements the Forest-R.K. Algorithm for Classification Problems

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rapportools 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-pkgKitten 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-mlbench 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rapportools 
Requires:         R-CRAN-partykit 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-pkgKitten 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-mlbench 

%description
Provides functions that calculates common types of splitting criteria used
in random forests for classification problems, as well as functions that
make predictions based on a single tree or a Forest-R.K. model; the
package also provides functions to generate importance plot for a
Forest-R.K. model, as well as the 2D multidimensional-scaling plot of data
points that are colour coded by their predicted class types by the
Forest-R.K. model. This package is based on: Bernard, S., Heutte, L.,
Adam, S., (2008, ISBN:978-3-540-85983-3) "Forest-R.K.: A New Random Forest
Induction Method", Fourth International Conference on Intelligent
Computing, September 2008, Shanghai, China, pp.430-437.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
