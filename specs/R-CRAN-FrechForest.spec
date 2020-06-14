%global packname  FrechForest
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          2%{?dist}
Summary:          Frechet Random Forests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-kmlShape 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-kmlShape 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-doParallel 
Requires:         R-graphics 

%description
Random forests are a statistical learning method widely used in many areas
of scientific research essentially for its ability to learn complex
relationships between input and output variables and also its capacity to
handle high-dimensional data. However, current random forests approaches
are not flexible enough to handle longitudinal heterogeneous data.  In
this package, we introduce Fréchet trees and Fréchet random forests, which
allow to manage data for which input and output variables are curves. To
this end, a new way of splitting the nodes of trees is introduced and the
prediction procedures of trees and forests are generalized.

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
