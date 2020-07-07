%global packname  bgmm
%global packver   1.8.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.4
Release:          3%{?dist}
Summary:          Gaussian Mixture Modeling Algorithms and the Belief-BasedMixture Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-combinat 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-car 
Requires:         R-lattice 
Requires:         R-CRAN-combinat 

%description
Two partially supervised mixture modeling methods: soft-label and
belief-based modeling are implemented. For completeness, we equipped the
package also with the functionality of unsupervised, semi- and fully
supervised mixture modeling.  The package can be applied also to selection
of the best-fitting from a set of models with different component numbers
or constraints on their structures. For detailed introduction see:
Przemyslaw Biecek, Ewa Szczurek, Martin Vingron, Jerzy Tiuryn (2012), The
R Package bgmm: Mixture Modeling with Uncertain Knowledge, Journal of
Statistical Software <doi:10.18637/jss.v047.i03>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
