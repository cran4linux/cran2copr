%global packname  BioFTF
%global packver   1.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Biodiversity Assessment Using Functional Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch

%description
The main drawback of the most common biodiversity indices is that
different measures may lead to different rankings among communities. This
instrument overcomes this limit using some functional tools with the
diversity profiles. In particular, the derivatives, the curvature, the
radius of curvature, the arc length, and the surface area are proposed.
The goal of this method is to interpret in detail the diversity profiles
and obtain an ordering between different ecological communities on the
basis of diversity. In contrast to the typical indices of diversity, the
proposed method is able to capture the multidimensional aspect of
biodiversity, because it takes into account both the evenness and the
richness of the species present in an ecological community.

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
