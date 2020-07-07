%global packname  ggstudent
%global packver   0.1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1.1
Release:          3%{?dist}
Summary:          Continuous Confidence Interval Plots using t-Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 

%description
Provides an extension to 'ggplot2' (Wickham, 2016,
<doi:10.1007/978-3-319-24277-4>) for creating two types of continuous
confidence interval plots (Violin CI and Gradient CI plots), typically for
the sample mean. These plots contain multiple user-defined confidence
areas with varying colours, defined by the underlying t-distribution used
to compute standard confidence intervals for the mean of the normal
distribution when the variance is unknown. Two types of plots are
available, a gradient plot with rectangular areas, and a violin plot where
the shape (horizontal width) is defined by the probability density
function of the t-distribution.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
