%global packname  W2CWM2C
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Graphical Tool for Wavelet (Cross) Correlation and WaveletMultiple (Cross) Correlation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-CRAN-waveslim 
BuildRequires:    R-CRAN-wavemulcor 
BuildRequires:    R-CRAN-colorspace 
Requires:         R-CRAN-waveslim 
Requires:         R-CRAN-wavemulcor 
Requires:         R-CRAN-colorspace 

%description
Set of functions that improves the graphical presentations of the
functions 'wave.correlation' and 'spin.correlation' (waveslim package,
Whitcher 2012) and the 'wave.multiple.correlation' and
'wave.multiple.cross.correlation' (wavemulcor package, Fernandez-Macho
2012b). The plot outputs (heatmaps) can be displayed in the screen or can
be saved as PNG or JPG images or as PDF or EPS formats. The W2CWM2C
package also helps to handle the (input data) multivariate time series
easily as a list of N elements (times series) and provides a multivariate
data set (dataexample) to exemplify its use. A description of the package
was published in Computing in Science & Engineering (Volume:16, Issue: 6)
on Sep. 09, 2014, doi:10.1109/MCSE.2014.96.

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
%{rlibdir}/%{packname}/INDEX
