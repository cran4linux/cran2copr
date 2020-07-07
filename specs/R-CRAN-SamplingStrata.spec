%global packname  SamplingStrata
%global packver   1.5-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          3%{?dist}
Summary:          Optimal Stratification of Sampling Frames for MultipurposeSampling Surveys

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-formattable 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-formattable 

%description
In the field of stratified sampling design, this package offers an
approach for the determination of the best stratification of a sampling
frame, the one that ensures the minimum sample cost under the condition to
satisfy precision constraints in a multivariate and multidomain case. This
approach is based on the use of the genetic algorithm: each solution (i.e.
a particular partition in strata of the sampling frame) is considered as
an individual in a population; the fitness of all individuals is evaluated
applying the Bethel-Chromy algorithm to calculate the sampling size
satisfying precision constraints on the target estimates. Functions in the
package allows to: (a) analyse the obtained results of the optimisation
step; (b) assign the new strata labels to the sampling frame; (c) select a
sample from the new frame accordingly to the best allocation. Functions
for the execution of the genetic algorithm are a modified version of the
functions in the 'genalg' package.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/figures
%{rlibdir}/%{packname}/INDEX
