%global packname  SGP
%global packver   1.9-0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.0.0
Release:          1%{?dist}
Summary:          Student Growth Percentiles & Percentile Growth Trajectories

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         tex(latex)
Requires:         tex(pdfpages)
BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-equate >= 2.0.5
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-sn >= 1.0.0
BuildRequires:    R-CRAN-randomNames >= 0.0.5
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-datasets 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doRNG 
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
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-sn >= 1.0.0
Requires:         R-CRAN-randomNames >= 0.0.5
Requires:         R-CRAN-Cairo 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-crayon 
Requires:         R-datasets 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doRNG 
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
Functions to calculate student growth percentiles and percentile growth
projections/trajectories for students using large scale, longitudinal
assessment data.  Functions use quantile regression to estimate the
conditional density associated with each student's achievement history.
Percentile growth projections/trajectories are calculated using the
coefficient matrices derived from the quantile regression analyses and
specify what percentile growth is required for students to reach future
achievement targets.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
