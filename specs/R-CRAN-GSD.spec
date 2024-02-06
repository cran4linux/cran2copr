%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GSD
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Graph Signal Decomposition

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-EbayesThresh 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-EbayesThresh 
Requires:         R-CRAN-ggplot2 

%description
Graph signals residing on the vertices of a graph have recently gained
prominence in research in various fields. Many methodologies have been
proposed to analyze graph signals by adapting classical signal processing
tools. Recently, several notable graph signal decomposition methods have
been proposed, which include graph Fourier decomposition based on graph
Fourier transform, graph empirical mode decomposition, and statistical
graph empirical mode decomposition. This package efficiently implements
multiscale analysis applicable to various fields, and offers an effective
tool for visualizing and decomposing graph signals. For the detailed
methodology, see Ortega et al. (2018) <doi:10.1109/JPROC.2018.2820126>,
Shuman et al. (2013) <doi:10.1109/MSP.2012.2235192>, Tremblay et al.
(2014)
<https://www.eurasip.org/Proceedings/Eusipco/Eusipco2014/HTML/papers/1569922141.pdf>,
and Cho et al. (2024) "Statistical graph empirical mode decomposition by
graph denoising and boundary treatment".

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
