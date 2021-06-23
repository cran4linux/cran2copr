%global __brp_check_rpaths %{nil}
%global packname  ecorest
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}%{?buildtag}
Summary:          Conducts Analyses Informing Ecosystem Restoration Decisions

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-viridis 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Three sets of data and functions for informing ecosystem restoration
decisions, particularly in the context of the U.S. Army Corps of
Engineers. First, model parameters are compiled as a data set and
associated metadata for over 500 habitat suitability models developed by
the U.S. Fish and Wildlife Service (USFWS 1980)
<https://www.fws.gov/policy/ESMindex.html>. Second, functions for
conducting habitat suitability analyses both for the models described
above as well as generic user-specified model parameterizations. Third, a
suite of decision support tools for conducting cost-effectiveness and
incremental cost analyses (Robinson et al. 1995)
<https://www.iwr.usace.army.mil/Portals/70/docs/iwrreports/95-R-1.pdf>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
