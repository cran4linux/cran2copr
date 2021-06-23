%global __brp_check_rpaths %{nil}
%global packname  cytominer
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Methods for Image-Based Cell Profiling

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0.76
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-futile.logger >= 1.4.3
BuildRequires:    R-Matrix >= 1.2
BuildRequires:    R-CRAN-tidyr >= 1.0.2
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-caret >= 6.0.76
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-futile.logger >= 1.4.3
Requires:         R-Matrix >= 1.2
Requires:         R-CRAN-tidyr >= 1.0.2
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-purrr >= 0.3.3

%description
Typical morphological profiling datasets have millions of cells and
hundreds of features per cell. When working with this data, you must clean
the data, normalize the features to make them comparable across
experiments, transform the features, select features based on their
quality, and aggregate the single-cell data, if needed. 'cytominer' makes
these steps fast and easy. Methods used in practice in the field are
discussed in Caicedo (2017) <doi:10.1038/nmeth.4397>. An overview of the
field is presented in Caicedo (2016) <doi:10.1016/j.copbio.2016.04.003>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
