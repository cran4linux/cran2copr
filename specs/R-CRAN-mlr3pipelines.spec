%global packname  mlr3pipelines
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}
Summary:          Preprocessing Operators and Pipelines for 'mlr3'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mlr3 >= 0.1.4
BuildRequires:    R-CRAN-mlr3misc >= 0.1.4
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-paradox 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-mlr3 >= 0.1.4
Requires:         R-CRAN-mlr3misc >= 0.1.4
Requires:         R-CRAN-backports 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-paradox 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-withr 

%description
Dataflow programming toolkit that enriches 'mlr3' with a diverse set of
pipelining operators ('PipeOps') that can be composed into graphs.
Operations exist for data preprocessing, model fitting, and ensemble
learning. Graphs can themselves be treated as 'mlr3' 'Learners' and can
therefore be resampled, benchmarked, and tuned.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
