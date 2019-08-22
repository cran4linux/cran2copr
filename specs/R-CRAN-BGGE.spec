%global packname  BGGE
%global packver   0.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.5
Release:          1%{?dist}
Summary:          Bayesian Genomic Linear Models Applied to GE Genome Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Application of genome prediction for a continuous variable, focused on
genotype by environment (GE) genomic selection models (GS). It consists a
group of functions that help to create regression kernels for some GE
genomic models proposed by Jarquín et al. (2014)
<doi:10.1007/s00122-013-2243-1> and Lopez-Cruz et al. (2015)
<doi:10.1534/g3.114.016097>. Also, it computes genomic predictions based
on Bayesian approaches. The prediction function uses an orthogonal
transformation of the data and specific priors present by Cuevas et al.
(2014) <doi:10.1534/g3.114.013094>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
