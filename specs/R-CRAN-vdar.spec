%global packname  vdar
%global packver   0.1.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2.1
Release:          2%{?dist}
Summary:          Discriminant Analysis Incorporating Individual Uncertainties

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-compositions 
Requires:         R-CRAN-compositions 

%description
The qda() function from package 'MASS' is extended to calculate a weighted
linear (LDA) and quadratic discriminant analysis (QDA) by changing the
group variances and group means based on cell-wise uncertainties. The
uncertainties can be derived e.g. through relative errors for each
individual measurement (cell), not only row-wise or column-wise
uncertainties. The method can be applied compositional data (e.g. portions
of substances, concentrations) and non-compositional data.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
