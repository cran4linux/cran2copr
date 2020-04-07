%global packname  mlrCPO
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}
Summary:          Composable Preprocessing Operators and Pipelines for MachineLearning

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-mlr >= 2.12
BuildRequires:    R-CRAN-checkmate >= 1.8.3
BuildRequires:    R-CRAN-BBmisc >= 1.11
BuildRequires:    R-CRAN-ParamHelpers >= 1.10
BuildRequires:    R-CRAN-backports >= 1.1.0
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-mlr >= 2.12
Requires:         R-CRAN-checkmate >= 1.8.3
Requires:         R-CRAN-BBmisc >= 1.11
Requires:         R-CRAN-ParamHelpers >= 1.10
Requires:         R-CRAN-backports >= 1.1.0
Requires:         R-CRAN-stringi 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Toolset that enriches 'mlr' with a diverse set of preprocessing operators.
Composable Preprocessing Operators ("CPO"s) are first-class R objects that
can be applied to data.frames and 'mlr' "Task"s to modify data, can be
attached to 'mlr' "Learner"s to add preprocessing to machine learning
algorithms, and can be composed to form preprocessing pipelines.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
