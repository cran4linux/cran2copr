%global packname  aws
%global packver   2.4-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.2
Release:          1%{?dist}
Summary:          Adaptive Weights Smoothing

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-awsMethods >= 1.1.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gsl 
Requires:         R-CRAN-awsMethods >= 1.1.1
Requires:         R-methods 
Requires:         R-CRAN-gsl 

%description
We provide a collection of R-functions implementing adaptive smoothing
procedures in 1D, 2D and 3D. This includes the Propagation-Separation
Approach to adaptive smoothing as described in "J. Polzehl and V. Spokoiny
(2006) <DOI:10.1007/s00440-005-0464-1>", "J. Polzehl and V. Spokoiny
(2004) <DOI:10.20347/WIAS.PREPRINT.998>" and "J. Polzehl, K. Papafitsoros,
K. Tabelow (2018) <DOI:10.20347/WIAS.PREPRINT.2520>", the Intersecting
Confidence Intervals (ICI), variational approaches and a non-local means
filter. Usage of the package is also described in Polzehl and Tabelow
(2019), Magnetic Resonance Brain Imaging, Appendix A, Springer, Use R!
Series. <doi:10.1007/978-3-030-29184-6_6>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install
test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R && echo "FFLAGS=$(R CMD config FFLAGS) -fallow-argument-mismatch" > ~/.R/Makevars
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
