%global packname  EML
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}
Summary:          Read and Write Ecological Metadata Language Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-emld >= 0.5.0
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-jqr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-emld >= 0.5.0
Requires:         R-CRAN-xml2 
Requires:         R-methods 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-jqr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-rmarkdown 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 

%description
Work with Ecological Metadata Language ('EML') files. 'EML' is a widely
used metadata standard in the ecological and environmental sciences,
described in Jones et al. (2006),
<doi:10.1146/annurev.ecolsys.37.091305.110031>.

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
