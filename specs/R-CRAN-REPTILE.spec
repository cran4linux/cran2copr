%global __brp_check_rpaths %{nil}
%global packname  REPTILE
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Regulatory DNA Element Prediction

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest >= 4.6.12
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-optparse >= 1.3.2
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-CRAN-flux >= 0.3.0
Requires:         R-CRAN-randomForest >= 4.6.12
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-optparse >= 1.3.2
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-CRAN-flux >= 0.3.0

%description
Predicting regulatory DNA elements based on epigenomic signatures. This
package is more of a set of building blocks than a direct solution.
REPTILE regulatory prediction pipeline is built on this R package. See
<https://github.com/yupenghe/REPTILE> for more information.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
