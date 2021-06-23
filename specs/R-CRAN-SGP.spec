%global __brp_check_rpaths %{nil}
%global packname  SGP
%global packver   1.9-5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.5.0
Release:          2%{?dist}%{?buildtag}
Summary:          Student Growth Percentiles & Percentile Growth Trajectories

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         tex(latex)
Requires:         tex(pdfpages.sty)
BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-equate >= 2.0.5
BuildRequires:    R-CRAN-doRNG >= 1.8.2
BuildRequires:    R-CRAN-rngtools >= 1.5
BuildRequires:    R-CRAN-data.table >= 1.12.4
BuildRequires:    R-CRAN-sn >= 1.0.0
BuildRequires:    R-CRAN-randomNames >= 0.0.5
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-datasets 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridBase 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-toOrdinal 
BuildRequires:    R-utils 
Requires:         R-CRAN-equate >= 2.0.5
Requires:         R-CRAN-doRNG >= 1.8.2
Requires:         R-CRAN-rngtools >= 1.5
Requires:         R-CRAN-data.table >= 1.12.4
Requires:         R-CRAN-sn >= 1.0.0
Requires:         R-CRAN-randomNames >= 0.0.5
Requires:         R-CRAN-Cairo 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-crayon 
Requires:         R-datasets 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-CRAN-gridBase 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-RSQLite 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-CRAN-toOrdinal 
Requires:         R-utils 

%description
An analytic framework for the calculation of norm- and
criterion-referenced academic growth estimates using large scale,
longitudinal education assessment data as developed in Betebenner (2009)
<doi:10.1111/j.1745-3992.2009.00161.x>.

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

%files
%{rlibdir}/%{packname}
