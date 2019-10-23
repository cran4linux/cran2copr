%global packname  Select
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Determines Species Probabilities Based on Functional Traits

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-lattice 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-FD 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-latticeExtra 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-lattice 
Requires:         R-graphics 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-FD 

%description
The objective of these functions is to derive a species assemblage that
satisfies a functional trait profile. Restoring resilient ecosystems
requires a flexible framework for selecting assemblages that are based on
the functional traits of species. However, current trait-based models have
been limited to algorithms that can only select species by optimising
specific trait values, and could not elegantly accommodate the common
desire among restoration ecologists to produce functionally diverse
assemblages. We have solved this problem by applying a non-linear
optimisation algorithm that optimises Rao Q, a closed-form functional
trait diversity index that incorporates species abundances, subject to
other linear constraints. This framework generalises previous models that
only optimised the entropy of the community, and can optimise both
functional diversity and entropy simultaneously. This package can also be
used to generate experimental assemblages to test the effects of
community-level traits on community dynamics and ecosystem function. The
method is based on theory discussed in Laughlin (2014, Ecology Letters)
<doi.org/10.1111/ele.12288>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
