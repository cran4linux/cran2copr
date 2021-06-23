%global __brp_check_rpaths %{nil}
%global packname  labourR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Classify Multilingual Labour Market Free-Text to StandardizedHierarchical Occupations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-cld2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stopwords 
BuildRequires:    R-CRAN-stringdist 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-cld2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stopwords 
Requires:         R-CRAN-stringdist 

%description
Allows the user to map multilingual free-text of occupations to a broad
range of standardized classifications. The package facilitates automatic
occupation coding (see, e.g., Gweon et al. (2017)
<doi:10.1515/jos-2017-0006> and Turrell et al. (2019)
<doi:10.3386/w25837>), where the ISCO to ESCO mapping is exploited to
extend the occupations hierarchy, Le Vrang et al. (2014)
<doi:10.1109/mc.2014.283>. Document vectorization is performed using the
multilingual ESCO corpus. A method based on the nearest neighbor search is
used to suggest the closest ISCO occupation.

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
