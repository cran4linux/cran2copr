%global packname  prevR
%global packver   3.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Regional Trends of a Prevalence from a DHS andSimilar Surveys

License:          CeCILL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rgdal >= 0.7
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-directlabels 
BuildRequires:    R-CRAN-GenKern 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-methods 
Requires:         R-CRAN-rgdal >= 0.7
Requires:         R-CRAN-sp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-directlabels 
Requires:         R-CRAN-GenKern 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-gstat 
Requires:         R-foreign 
Requires:         R-CRAN-maptools 
Requires:         R-methods 

%description
Spatial estimation of a prevalence surface or a relative risks surface,
using data from a Demographic and Health Survey (DHS) or an analog survey,
see Larmarange et al. (2011) <doi:10.4000/cybergeo.24606>.

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
