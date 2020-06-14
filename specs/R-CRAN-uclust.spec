%global packname  uclust
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Clustering and Classification Inference with U-Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-robcor 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-robcor 

%description
Clustering and classification inference for high dimension low sample size
(HDLSS) data with U-statistics. The package contains implementations of
nonparametric statistical tests for sample homogeneity, group separation,
clustering, and classification of multivariate data. The methods have high
statistical power and are tailored for data in which the dimension L is
much larger than sample size n. See Gabriela B. Cybis, Marcio Valk and
Sílvia RC Lopes (2018) <doi:10.1080/00949655.2017.1374387> and Marcio Valk
and Gabriela B. Cybis (2018) <arXiv:1805.12179>.

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
