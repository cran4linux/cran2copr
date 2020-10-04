%global packname  sdm
%global packver   1.0-89
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.89
Release:          3%{?dist}%{?buildtag}
Summary:          Species Distribution Modelling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp >= 1.2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
Requires:         R-CRAN-sp >= 1.2.0
Requires:         R-methods 
Requires:         R-CRAN-raster 

%description
An extensible framework for developing species distribution models using
individual and community-based approaches, generate ensembles of models,
evaluate the models, and predict species potential distributions in space
and time. For more information, please check the following paper: Naimi,
B., Araujo, M.B. (2016) <doi:10.1111/ecog.01881>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/external
%doc %{rlibdir}/%{packname}/methods
%doc %{rlibdir}/%{packname}/quick_sdm.Rmd
%doc %{rlibdir}/%{packname}/shinyApps
%doc %{rlibdir}/%{packname}/test
%{rlibdir}/%{packname}/INDEX
