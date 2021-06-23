%global __brp_check_rpaths %{nil}
%global packname  EcoTroph
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          3%{?dist}%{?buildtag}
Summary:          EcoTroph R package

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-XML 

%description
EcoTroph is an approach and software for modelling marine and freshwater
ecosystems. It is articulated entirely around trophic levels. EcoTroph's
key displays are bivariate plots, with trophic levels as the abscissa, and
biomass flows or related quantities as ordinates. Thus, trophic ecosystem
functioning can be modelled as a continuous flow of biomass surging up the
food web, from lower to higher trophic levels, due to predation and
ontogenic processes. Such an approach, wherein species as such disappear,
may be viewed as the ultimate stage in the use of the trophic level metric
for ecosystem modelling, providing a simplified but potentially useful
caricature of ecosystem functioning and impacts of fishing. This version
contains catch trophic spectrum analysis (CTSA) function and corrected
versions of the mf.diagnosis and create.ETmain functions.

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
%{rlibdir}/%{packname}/INDEX
