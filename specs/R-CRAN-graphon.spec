%global __brp_check_rpaths %{nil}
%global packname  graphon
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          3%{?dist}%{?buildtag}
Summary:          A Collection of Graphon Estimation Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ROptSpace 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ROptSpace 
Requires:         R-utils 
Requires:         R-CRAN-Rdpack 

%description
Provides a not-so-comprehensive list of methods for estimating graphon, a
symmetric measurable function, from a single or multiple of observed
networks. For a detailed introduction on graphon and popular estimation
techniques, see the paper by Orbanz, P. and Roy, D.M.(2014)
<doi:10.1109/TPAMI.2014.2334607>. It also contains several auxiliary
functions for generating sample networks using various network models and
graphons.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
